# 🧠 Black Box Endpoint Analysis

## 🛠 Methodology

Each endpoint was tested using a series of crafted JSON inputs. Responses were observed, logged, and patterns were analyzed to reverse-engineer each endpoint’s behavior.

---

## 🔍 Endpoint: `/api/example` (Replace with real path)

- **Method**: POST
- **Expected Input**: JSON with a field `"input"`
- **Behavior Observed**:
  - If input is a string, it returns reversed content.
  - If input is numeric, it returns the square.
  - Empty string returns a default message.

- **Sample Input/Output**:

| Input | Output |
|-------|--------|
| `"hello"` | `"olleh"` |
| `"1234"`  | `"1522756"` |
| `""`      | `"No input provided"` |

---

(Repeat for all other endpoints)
