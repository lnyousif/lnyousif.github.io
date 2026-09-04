---
title: Baghdad to Brooklyn
icon: fas fa-book
order: 4
description: Baghdad to Brooklyn — An Ordinary Journey Through Extraordinary Times. Laith Yousif's memoir of Baghdad, Dubai and New York. Out now, a Kirkus Reviews "Get It" pick.
image: /assets/img/book-cover.jpg
---

<!-- TODO (Laith): swap for the canonical Amazon link when you have it.
     Built from ASIN B0HHG9M6J1. -->
{% assign amazon_url = 'https://www.amazon.com/dp/B0HHG9M6J1' %}

{% assign book_cover = site.static_files | where: 'path', '/assets/img/book-cover.jpg' | first %}

<link rel="stylesheet" href="{{ '/assets/css/author-home.css' | relative_url }}" />

<div class="ly-home ly-bookpage">
  <p class="ly-book__sub">An Ordinary Journey Through Extraordinary Times &mdash; a memoir by Laith Yousif</p>

  <div class="ly-book__top">
    <div>
      <p class="ly-hook">
        I left Baghdad to get away from buildings getting blown up. I moved to
        New York. My first job was in the World Trade Center. Then 9/11 happened.
      </p>

      <div class="ly-cta">
        <a class="ly-btn ly-btn--primary" href="{{ amazon_url }}" target="_blank" rel="noopener noreferrer">
          Buy the print edition &rarr;
        </a>
        <a class="ly-btn ly-btn--ghost" href="#excerpt">Read an excerpt</a>
      </div>

      <a class="ly-kirkus"
         href="https://www.kirkusreviews.com/book-reviews/laith-yousif/baghdad-to-brooklyn/"
         target="_blank" rel="noopener noreferrer">
        <span class="ly-kirkus__stamp">Get It</span>
        <span class="ly-kirkus__who">Kirkus Reviews</span>
        <span class="ly-kirkus__what">Read the review &rarr;</span>
      </a>
    </div>

    {% if book_cover %}
      <div class="ly-cover">
        <img src="{{ '/assets/img/book-cover.jpg' | relative_url }}"
             alt="Cover of Baghdad to Brooklyn, a memoir by Laith Yousif"
             width="400" height="600" />
      </div>
    {% endif %}
  </div>

  <p class="ly-synopsis">
    A boy grows up in Al-Dora, in a house his father built by working for free.
    A young engineer leaves Iraq in 1998 with a borrowed $700 and a passport
    someone else is holding. A new New Yorker walks into the World Trade Center
    on March 26, 2001. <i>Baghdad to Brooklyn</i> is the story of what happened
    next, and the ten years of waiting that followed.
  </p>

  <!-- The long-form material lives on the city hubs, not on this page. -->
  <section class="ly-section">
    <div class="ly-section__head">
      <h2>Three cities, one story</h2>
      <span class="ly-lbl">Read on</span>
    </div>
    <div class="ly-doors">
      <a class="ly-door" href="{{ '/baghdad/' | relative_url }}">
        <span class="ly-door__city">Baghdad</span>
        <span class="ly-door__years">1972&ndash;1998</span>
        <span class="ly-door__go">Enter Baghdad &rarr;</span>
      </a>
      <a class="ly-door" href="{{ '/dubai/' | relative_url }}">
        <span class="ly-door__city">Dubai</span>
        <span class="ly-door__years">1998&ndash;2001</span>
        <span class="ly-door__go">Enter Dubai &rarr;</span>
      </a>
      <a class="ly-door" href="{{ '/new-york/' | relative_url }}">
        <span class="ly-door__city">New York</span>
        <span class="ly-door__years">2001&ndash;present</span>
        <span class="ly-door__go">Enter New York &rarr;</span>
      </a>
    </div>
  </section>

  <section class="ly-section" id="excerpt">
    <div class="ly-section__head">
      <h2>Excerpt</h2>
    </div>
    <!-- TODO (Laith): paste an excerpt here; the homepage links straight to it. -->
    <p class="ly-muted-note">Coming soon.</p>
  </section>

  <section class="ly-section">
    <div class="ly-section__head">
      <h2>The details</h2>
      <span class="ly-lbl">Publication</span>
    </div>
    <dl class="ly-facts">
      <div><dt>Publisher</dt><dd>Manhattan Book Group</dd></div>
      <div><dt>Published</dt><dd>August 25, 2026</dd></div>
      <div><dt>ISBN</dt><dd>979-8950391057</dd></div>
      <div><dt>ASIN</dt><dd>B0HHG9M6J1</dd></div>
      <div><dt>Editions</dt><dd>Print now &middot; eBook and audiobook to come</dd></div>
    </dl>
    <p class="ly-muted-note">
      Behind the book: the <a href="{{ '/pages/fbtny/' | relative_url }}">blog that became its first draft</a>,
      and <a href="{{ '/categories/baghdad-to-brooklyn/' | relative_url }}">posts from the writing years</a>.
    </p>
  </section>

  <section class="ly-section ly-close" id="press">
    <div class="ly-section__head">
      <h2>For press &amp; media</h2>
      <span class="ly-lbl">Contact</span>
    </div>
    <p class="ly-close__body">
      The press kit has the bio, three story angles, book details, interview
      availability and a downloadable one-sheet. No gatekeeper &mdash; email
      goes straight to me.
    </p>
    <dl class="ly-press__contact">
      <dt>Press contact</dt>
      <dd><a href="mailto:Laith@LaithYousif.com?subject=Press%20enquiry%20%E2%80%94%20Baghdad%20to%20Brooklyn">Laith@LaithYousif.com</a></dd>
    </dl>
    <div class="ly-press__links">
      <a class="ly-btn ly-btn--primary" href="{{ '/press/' | relative_url }}">Press kit &rarr;</a>
      <a class="ly-btn ly-btn--ghost" href="{{ '/press/Baghdad_to_Brooklyn_Anniversary_One_Sheet.pdf' | relative_url }}">
        <i class="fas fa-file-pdf" aria-hidden="true"></i> One-sheet (PDF)
      </a>
    </div>
  </section>
</div>
