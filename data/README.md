# LexUz Offline Dataset (Uzbekistan Laws)

## Description
This dataset contains the complete collection of Uzbekistan laws and regulations extracted from the Lex.uz Offline application. It includes over 141,000 legal acts in Uzbek (Latin) script.

## Files
- **lex_uz_metadata.csv**: Contains basic information about each law (ID, Title, Acceptance Date, Document Number, and Status).
- **lex_uz_unified.jsonl**: Contains the full text of each law along with its metadata. The text has been cleaned of HTML tags.
- **ldb.db**: The original SQLite database for advanced querying.

## Data Schema (CSV & JSONL)
- `id`: Unique identifier for the document.
- `title`: The title of the law/regulation.
- `acceptance_date`: The date when the act was officially accepted.
- `doc_number`: Official document registration number.
- `content`: Cleaned full text of the legal act.

## Statistics
- Total Documents: 141,912
- Language: Uzbek (Latin)
- Source: Lex.uz Offline (Sept 2025 version)
