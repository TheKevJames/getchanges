<a name="0.1.0"></a>
## 0.1.0 (2019-02-02)

#### Features

* **cli:**  hide stack traces behind --verbose ([039477d7](039477d7))

#### Bug Fixes

* **cli:**  avoid bad error when piping into pager ([890564f6](890564f6))

<a name="0.0.3"></a>
## 0.0.3 (2018-09-12)

#### Bug Fixes

* **cli:**  allow usage without explicit installation ([9c1bb62d](9c1bb62d))

#### Compatibility

*  drop (broken) support for Python 3.5 ([3426438e](3426438e))

<a name="0.0.2"></a>
## 0.0.2 (2018-09-11)

#### Features

* **sources:**
  *  support `release*` folders ([4c768750](4c768750))
  *  support `release*` files ([622d39a0](622d39a0))
  *  support `HISTORY` files ([a99a3ca4](a99a3ca4))

#### Bug Fixes

* **github:**  support urls with included ".git" ([8a6fea1f](8a6fea1f))
* **pypi:**  avoid breaking when `project_urls=None` ([8be35027](8be35027))

<a name="0.0.1"></a>
## 0.0.1 (2018-09-10)

#### Features

* **sources:**
  *  initial work on getchanges (annotated pypi support) ([a7952f7e](a7952f7e))
  *  add rtfd support ([d8ce66fd](d8ce66fd))
  *  support "code" pypi urls ([655c1136](655c1136))
  *  "support" github release notes ([62339f8f](62339f8f))

#### Bug Fixes

* **github:**  support github urls with trailing slashes ([2631be26](2631be26))
* **pypi:**  do not attempt to access null `project_urls` ([4d9a4fbb](4d9a4fbb))
