# Specmatic Testing Example

[![Check Contracts](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/contracts.yaml)
[![Validate Action](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/versions.yaml)
[![Lint OpenAPI](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml/badge.svg)](https://github.com/sergeyklay/specmatic-testing-example/actions/workflows/lint.yaml)

This project contains the product API, which can used by client applications.
Here is the [contract](https://github.com/sergeyklay/specmatic-testing-example/blob/main/contracts/documentation.yaml)
governing the interaction of the client with the product API.

## Requirements
- Python 3.8 >= 3.8
- SQLite3
- Node.js >= 16

## How to try it out

### Install dependencies and tools

1. First, install Python dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

2. Run database migrations
   ```bash
   flask --app runner:app db upgrade
   ```

3. Run database seed
   ```bash
   flask --app runner:app seed
   ```

4. Next, install Node.js linters and tools:
   ```bash
   npm install
   ```

5. Finally, install [specmatic](https://specmatic.in/download/latest.html).

### Run API server

To run API server use the command as follows:

```bash
flask --app runner:app run
```

### Run the contract tests

To run contract tests use the command as follows:

```bash
java -jar specmatic.jar test --testBaseURL=http://127.0.0.1:5000
```

### Run lint check

To run code style checking use the command as follows:

```bash
npm run lint
```

## Support

Should you have any question, any remark, or if you find a bug, or if there is something
you can't do with the Specmatic Testing Example, please
[open an issue](https://github.com/sergeyklay/specmatic-testing-example/issues).

## License

Specmatic Testing Example licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more information.
