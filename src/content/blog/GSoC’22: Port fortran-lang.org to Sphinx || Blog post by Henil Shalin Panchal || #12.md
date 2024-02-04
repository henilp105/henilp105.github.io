---
author: Henil Panchal
pubDatetime: 2022-09-23T15:22:00Z
modDatetime: 2023-12-21T09:12:47.400Z
title: "GSoC’22: Port fortran-lang.org to Sphinx || Blog post by Henil Shalin Panchal || #12"
slug: "gsoc’22:-port-fortran-lang.org-to-sphinx-||-blog-post-by-henil-shalin-panchal-||-#12"
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
description: "GSoC’22: Port fortran-lang.org to Sphinx || Blog post by Henil Shalin Panchal || #12"
---

Greetings of the Day Everyone!
We plan to finish the migration by end of next week. Next step is to add a banner to the current page to make visitors aware of the upcoming migration.
Once we migrated to the sphinx based webpage this repository will be available at the default GH pages URL https://fortran-lang.github.io/fortran-lang.org and we will create a banner on the new webpage referencing the old repository in case somebody finds something missing.
This week as we have decided to shift the sphinx site to a new repo (https://github.com/fortran-lang/webpage), I have ported the sphinx site to my fork of new repo and also added various functionalities like:

- [x] resolves #56
- [x] resolves #115
- [x] resolves #116
- [x] resolves rss feed url on nav bar.
- [x] prettified files.
- [x] resolves #118

- [x] resolves #41

- [x] resolves #43

- [x] set prettier in pre-commit hooks

- [x] GNU license link in intrinsics.

- [x] resolves the setup python bug #4 ( there was a bug in v4 which prevented the detection of python version , setting that version of python manually resolves the bug.)

- [x] resolves the ablog #36 dependabot pr.

- [x] github pages url for pr preview.

- [x] resolves the learn section button translation bug

- [x] updated the translations for learn section button.

- [x] shift from custom navbar to original navbar

- [x] learn section dark theme color fixed.

- [x] resolves #39
- [x] announcement banner for the new site of fortran-lang.org
      I will be maintaining my fortran-lang's github pages here : https://fortran-lang.github.io/webpage/en/index.html
      The link of the Github pages has been changed to avoid build conflicts and to preserve the existing site at a subdomain.All the changes can be found at my fork's github pages.

All the pages of the website are being rendered by Sphinx only.
Please feel free to ping me here or on my mail: [henilp105@gmail.com](mailto:henilp105@gmail.com).
I will be regularly posting the weekly blog links [here](https://docs.google.com/document/d/1Et-2JPlnA9SAssSnmzkYeXQ1ExXqBI5tcdBQhuqvilE/edit?usp=sharing).
Thanks and Regards,
Henil Shalin Panchal
