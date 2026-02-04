from lxml import etree
from database.db import get_db, init_db

RESULTS_FILE = "results.xml"

def main():
    init_db()

    tree = etree.parse(RESULTS_FILE)
    root = tree.getroot()

    db = get_db()

    inserted = 0

    for case in root.findall(".//testcase"):
        failure = case.find("failure")
        error = case.find("error")

        if failure is not None or error is not None:
            node = failure if failure is not None else error
            message = node.get("message") or "No message"

            db.execute(
                "INSERT INTO test_failure(test_name, error_message) VALUES (?, ?)",
                (case.get("name"), message)
            )
            inserted += 1

    db.commit()
    db.close()

    print(f"Saved {inserted} failures into test_results.db")

if __name__ == "__main__":
    main()
