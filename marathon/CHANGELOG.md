# CHANGELOG - marathon

## 1.12.0 / 2020-01-13

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.11.0 / 2019-12-02

* [Added] Add auth type to RequestsWrapper. See [#4708](https://github.com/DataDog/integrations-core/pull/4708).

## 1.10.0 / 2019-10-11

* [Added] Add option to override KRB5CCNAME env var. See [#4578](https://github.com/DataDog/integrations-core/pull/4578).

## 1.9.0 / 2019-08-24

* [Added] Add request wrapper to marathon. See [#4324](https://github.com/DataDog/integrations-core/pull/4324).

## 1.8.0 / 2019-07-13

* [Added] Add log section. See [#4014](https://github.com/DataDog/integrations-core/pull/4014).

## 1.7.0 / 2019-05-14

* [Added] Adhere to code style. See [#3536](https://github.com/DataDog/integrations-core/pull/3536).

## 1.6.0 / 2019-02-18

* [Added] Support Python 3. See [#2871](https://github.com/DataDog/integrations-core/pull/2871).

## 1.5.0 / 2018-10-12

* [Fixed] Removed default arguments from process_apps. See [#2337][1].
* [Added] Add ability to tag metrics based on marathon labels. See [#2165][2]. Thanks [ashirley][3].

## 1.4.1 / 2018-09-04

* [Fixed] Add data files to the wheel package. See [#1727][4].

## 1.4.0 / 2018-06-07

* [Fixed] Ensure marathon queue count reports 0 for apps not in queue. See [#1548][5].
* [Changed] [marathon] add task counts metrics for groups. See [#1513][6].

## 1.3.0 / 2018-05-11

* [FEATURE] Adds custom tag support for service checks.

## 1.2.1 / 2018-01-10

* [BUGFIX] Fix duplicate `app:` tags on app-level metrics. See [#987][7], thanks [@emil-applause][8]

## 1.2.0 / 2017-08-28

* [FEATURE] Adds v2 queue metrics. See [#464][9]

## 1.1.0 / 2017-07-18

* [FEATURE] Add gauge for queue size. See [#321][10], thanks [@jangie][11]

## 1.0.0 / 2017-03-22

* [FEATURE] adds marathon integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2337
[2]: https://github.com/DataDog/integrations-core/pull/2165
[3]: https://github.com/ashirley
[4]: https://github.com/DataDog/integrations-core/pull/1727
[5]: https://github.com/DataDog/integrations-core/pull/1548
[6]: https://github.com/DataDog/integrations-core/pull/1513
[7]: https://github.com/DataDog/integrations-core/issues/987
[8]: https://github.com/emil-applause
[9]: https://github.com/DataDog/integrations-core/issues/464
[10]: https://github.com/DataDog/integrations-core/issues/321
[11]: https://github.com/jangie