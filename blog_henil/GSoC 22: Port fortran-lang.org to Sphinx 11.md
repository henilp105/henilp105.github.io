---
author: Henil Panchal
pubDatetime: 2022-09-23T15:22:00Z
modDatetime: 2023-12-21T09:12:47.400Z
title: "GSoC’22: Port fortran-lang.org to Sphinx || Blog post by Henil Shalin Panchal || #11"
slug: "gsoc’22:-port-fortran-lang.org-to-sphinx-||-blog-post-by-henil-shalin-panchal-||- 11"
featured: true
draft: false
tags:
  - docs
  - Google Summer of Code'22
  - GSoC'22
  - fortran-lang.org
  - Sphinx
  - Fortran
  - Jinja
  - Python
description: "GSoC’22: Port fortran-lang.org to Sphinx || Blog post by Henil Shalin Panchal || #11"
---

Greetings of the Day Everyone!
This week as we have decided to shift the sphinx site to a new repo (https://github.com/fortran-lang/webpage), I have ported the sphinx site to my fork of new repo and also added various functionalities like:

- [x] resolves the setup python bug #4 ( there was a bug in v4 which prevented the detection of python version , setting that version of python manually resolves the bug.)
- [x] resolves the ablog #36 dependabot pr.
- [x] github pages url for pr preview.
- [x] resolves the learn section button translation bug
- [x] updated the translations for learn section button.
- [x] shift from custom navbar to original navbar
- [x] added pr preview banner for preview builds. (independent of the pydata theme version).
- [x] added documentation for pre-commit hooks.
- [x] locked the dependency versions of packages.
- [x] Formated the html templates.
- [x] resolved the date error in newsletter of june 2022.
- [x] enabled build of all translations for build preview
- [x] resolved #29 (for index page)
- [x] added dependabot for requirements.txt
- [x] updated translations

* [Incorrect layout for window width > 600 and < 720 pixels #6](https://github.com/fortran-lang/webpage/issues/6)
* [Have package, minibook and contributing guidelines as part of the webpage #7](https://github.com/fortran-lang/webpage/issues/7)
* [Linting / Stylechecking of Python scripts #9](https://github.com/fortran-lang/webpage/issues/9)
* [Should we consistently use MyST-Markdown? #10](https://github.com/fortran-lang/webpage/issues/10)
  I will be maintaining my fortran-lang's github pages here : https://fortran-lang.github.io/webpage/en/index.html
  All the pages of the website are being rendered by Sphinx only.
  Please feel free to ping me here or on my mail: [henilp105@gmail.com](mailto:henilp105@gmail.com).
  I will be regularly posting the weekly blog links [here](https://docs.google.com/document/d/1Et-2JPlnA9SAssSnmzkYeXQ1ExXqBI5tcdBQhuqvilE/edit?usp=sharing).

Thanks and Regards,
Henil Shalin Panchal
CC @awvwgk @rgoswami
