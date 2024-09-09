# ScrambledLibrary

ScrambledLibrary is a Python package that transforms sentences into new ones using three unique scrambling methods.

## Installation

Install ScrambledLibrary using pip:
```bash
pip install scrambled-library
```

## Usage
```python
from scrambled_library import deviled_scramble, sunnysideup_scramble, double_yolk_scramble

text = "The quick brown fox jumps over the lazy dog"

print(sunnysideup_scramble(text))
```

### Scrambling Methods

There are currently 3 you can use: Deviled, SunnySideUp, or Doubleyolk. To use them, just import the corresponding method. Each of them are different in it's own way, give each of them a try!

### Optional File Output

Each method accepts an `output_to_file` parameter:

```python
deviled_scramble(text, output_to_file=True)
```
This will save the result to a text file (e.g., `deviled_output.txt`).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

[Your Name or Username]

GitHub: [@The-Hipnotist](https://github.com/The-Hipnotist)
