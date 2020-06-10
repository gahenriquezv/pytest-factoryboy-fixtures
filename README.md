# FixtureGenerator
Generates pytest fixtures that allow the use of type hinting (MyPy or PyCharm).

## Usage
`cli.py class1,class2,...`

Example:

```
>>> cli.py PascalCase,camelCase,snake_case

@fixture
def pascal_case() -> PascalCase:
    return PascalCaseFactory()

@fixture
def pascal_case_factory() -> Union[Type[PascalCase], Type[PascalCaseFactory]]:
    return PascalCaseFactory

@fixture
def camel_case() -> CamelCase:
    return CamelCaseFactory()

@fixture
def camel_case_factory() -> Union[Type[CamelCase], Type[CamelCaseFactory]]:
    return CamelCaseFactory

@fixture
def snake_case() -> SnakeCase:
    return SnakeCaseFactory()

@fixture
def snake_case_factory() -> Union[Type[SnakeCase], Type[SnakeCaseFactory]]:
    return SnakeCaseFactory
```
stdout/stdin can be used to write a file instead.
```
>>> cli.py runTest1,runTest2 > fixtures.py
```
