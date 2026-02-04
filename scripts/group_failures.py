import re
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from database.db import DB_NAME

def clean(text: str) -> str:
    if not text:
        return ""
    t = text.lower()

    # remove common pytest noise
    t = t.replace("assert false", " ")
    t = re.sub(r"assert\s+\d+\s*==\s*\d+", " ", t)

    # keep only first line (usually best signal)
    t = t.splitlines()[0]

    # remove "assertionerror:" etc. (optional)
    t = t.replace("assertionerror:", " ")
    t = t.replace("timeouterror:", " ")
    t = t.replace("error:", " ")

    # normalize spaces
    t = re.sub(r"\s+", " ", t).strip()
    return t

def main():
    db = sqlite3.connect(DB_NAME)
    rows = db.execute("SELECT id, test_name, error_message FROM test_failure").fetchall()

    if not rows:
        print("No failures found in DB. Run read_results first.")
        return

    raw_texts = [r[2] for r in rows]
    texts = [clean(t) for t in raw_texts]   # ✅ cleaned texts

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    k = min(4, len(texts))
    labels = KMeans(n_clusters=k, random_state=0, n_init="auto").fit_predict(X)

    # save into DB
    for (failure_id, _, _), label in zip(rows, labels):
        db.execute("UPDATE test_failure SET group_id=? WHERE id=?", (int(label), failure_id))
    db.commit()
    db.close()

    # print groups
    print("\n=== Failure Groups (Saved to DB) ===")
    groups = {}
    for (failure_id, test_name, message), label in zip(rows, labels):
        groups.setdefault(int(label), []).append((failure_id, test_name, message))

    for group_id, items in groups.items():
        print(f"\n--- Group {group_id} ({len(items)} failures) ---")
        for failure_id, test_name, message in items:
            print(f"[{failure_id}] {test_name}: {message.splitlines()[0]}")

if __name__ == "__main__":
    main()
