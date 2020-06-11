# pytest-factoryboy-fixtures
Writes pytest fixtures for FactoryBoy with type hinting. The hints allow for proper code completion in your tests when using PyCharm. 

## Usage
`pytest-factoryboy-fixtures [comma seperated class names]`

Add the generated code to your `conftest.py`.

### Example

`>>> pytest-factoryboy-fixtures FirstClass,SecondClass`
```python
    @fixture
    def first_class() -> FirstClass:
        return FirstClassFactory()
        
        
    @fixture
    def first_class_factory() -> Union[Type[FirstClass], Type[FirstClassFactory]]:
        return FirstClassFactory
        
        
    @fixture
    def second_class() -> SecondClass:
        return SecondClassFactory()
        
        
    @fixture
    def second_class_factory() -> Union[Type[SecondClass], Type[SecondClassFactory]]:
        return SecondClassFactory
```

