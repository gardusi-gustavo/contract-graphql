# package-graphql

Pure GraphQL SDL contract registry.

## Layout

| `schema/common.graphql` | pagination and errors |
| `schema/dataset.graphql` | dataset queries |
| `schema/ingestion.graphql` | ingestion mutations |

## Validation

```bash
bash infra/scripts/ci.sh
```

## Rules

- Public contract/asset package only.
- No application data, secrets, or personal data.
- Versioned by tag.
