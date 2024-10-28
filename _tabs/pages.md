---
layout: page
icon: far fa-copy
order: 4
# All the Pages of the website
---
{% include lang.html %}


<div id="pages" class="pl-xl-3">
  {% for page in site.pages %}


    <li>
      <span class="date day" data-ts="{{ ts }}" data-df="DD">     </span>
      <span class="date month small text-muted ms-1" >
    
      </span>

      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    </li>


  {% endfor %}
</div>
