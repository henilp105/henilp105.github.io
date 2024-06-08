---
layout: page
title: Papershelf
permalink: /papershelf/
description:
nav: true
nav_order: 2
horizontal: false
---


<div class="papers">
<h4> I read a few papers every week around various topics that interests me and here are some of them that I found amusing.<h4>
  <h2>Read</h2>
  {%- assign reading_papers = site.data.papers | where: "status", "reading" %}
  <div class="paper-list">
  <ul>
    {%- for paper in reading_papers -%}
   <li> <h5><a href="{{ paper.arxiv_url }}">{{ paper.title }}</a></h5></li>
    {%- endfor %}
    </ul>
  </div>

  <h2>To Be Read</h2>
  {%- assign to_be_read_papers = site.data.papers | where: "status", "to-be-read" %}

  <div class="paper-list">
  <ul>
    {%- for paper in to_be_read_papers -%}
    <li> <h5><a href="{{ paper.arxiv_url }}">{{ paper.title }}</a></h5></li>
    {%- endfor %}
    </ul>
  </div>
