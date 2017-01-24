History/Changelog
=================

1.0.3
-----

- Use flake8-polyfill to get standard-in to handle Flake8 3.x and 2.x

1.0.2
-----

- Use pycodestyle to get standard-in.

1.0.1
-----

- Make sure this works out of the box (is enabled by default) with Flake8 3.0

1.0.0
-----

- Switch dependency name to pydocstyle. pep257 was renamed to pydocstyle, this
  update switches the requirement to that new package name. Since we're
  swapping out dependencies, we've issued a major version bump.

0.2.7
-----

- Try to import pydocstyle (not pycodestyle) as pep257

0.2.6
-----

- Respect pep257's default ignore list

- Handle AllError and other exceptions from pep257

0.2.5
-----

- Use pep257's ``tokenize_open`` function to pass input to the tool.

- Use pep257's conventions so any error codes that are ignored by default
  using ``pep257`` are also ignored by default with this plugin.

0.2.4
-----

- Fix bug introduced in 0.2.2 where the file source was always None causing
  D100 and D104 errors for all files and no other errors to be found.

0.2.3
-----

- Remove extraneous space in error message.

- Fix up how the plugin displays with ``flake8 --version``.

0.2.2
-----

- Better support for input provided via stdin.

0.2.1
-----

- Prevent AllError or EnvironmentErrors from being raised. Thanks Alex
  Pyrgiotis.

0.2.0
-----

- Upgrade to pep257 0.3.0

0.1.4
-----

- Stop truncating error messages

0.1.3
-----

- Really fix the installation issue this time.

0.1.2
-----

- Actually fix the PyPI release. **Ugh**

0.1.1
-----

- Fix the PyPI release.

0.1.0
-----

- Initial Release!
