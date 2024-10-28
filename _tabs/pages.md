---
layout: page
icon: far fa-copy
order: 4
# All the Pages of the website
---
{% include lang.html %}


<div id="pages" class="pl-xl-3">
  {% for page in site.pages %}


    
<span style="width: 25px;  height: 10px; display: inline-block;"></span>

      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    <br/>


  {% endfor %}
</div>
