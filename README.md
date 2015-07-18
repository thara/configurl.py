# configurl

Use 12factor inspired URLs to configure any applications.

**This project is in development. It has not been released yet.**

## Usage

Parse setting from URL string:

```
import configurl
setting = configurl.parse("https://user:password@127.0.0.1:8080")

assert setting["SCHEME"] = "https"
assert setting["USER"] = "user"
assert setting["PASSWORD"] = "password"
assert setting["HOST"] = "127.0.0.1"
assert setting["PORT"] = 8080
```

## Requirements

- Python 3.4+

I will support Python 2.6+.


## VS. 

If you want to configure database only on your Django applications, you can use [dj-database-url](https://github.com/kennethreitz/dj-database-url).

**** is generaized than [dj-database-url](https://github.com/kennethreitz/dj-database-url) so it make to write some code for converting to database engine from scheme on Django applications.


## Licence

[MIT](https://github.com/tomochikahara/configurl.py/blob/master/LICENCE)

## Author

[Tomochika Hara](https://github.com/tomochikahara)

