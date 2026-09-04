---
title: Baghdad to Brooklyn
icon: fas fa-book
order: 4
description: Baghdad to Brooklyn — An Ordinary Journey Through Extraordinary Times. Laith Yousif's memoir of Baghdad, Dubai and New York. Out now, reviewed by Kirkus.
# TODO: swap to /assets/img/book-cover.jpg once the cover art is added.
image: /assets/img/avatar.png
---

<!-- TODO (Laith): swap for the canonical Amazon link when you have it.
     Built from ASIN B0HHG9M6J1. -->
{% assign amazon_url = 'https://www.amazon.com/dp/B0HHG9M6J1' %}

<!-- TODO (Laith): drop the cover art at assets/img/book-cover.jpg and it
     appears here automatically — no code change needed. -->
{% assign book_cover = site.static_files | where: 'path', '/assets/img/book-cover.jpg' | first %}

*An Ordinary Journey Through Extraordinary Times — a memoir by Laith Yousif*

{% if book_cover %}
<img src="{{ '/assets/img/book-cover.jpg' | relative_url }}"
     alt="Cover of Baghdad to Brooklyn, a memoir by Laith Yousif"
     width="300" height="450"
     style="width:min(300px,60%);height:auto;aspect-ratio:2/3;object-fit:cover;border-radius:6px" />
{% endif %}

---

> **📖 Out now.**
> After more than twenty years of writing this life down in pieces, the book is here.
>
> **[Buy the print edition on Amazon →]({{ amazon_url }})**
>
> <!-- TODO (Laith): add eBook and audiobook links here once they are released. -->
> eBook and audiobook editions are not out yet.

<link rel="stylesheet" href="{{ '/assets/css/author-home.css' | relative_url }}" />
<div class="ly-home">
  <a class="ly-kirkus"
     href="https://www.kirkusreviews.com/book-reviews/laith-yousif/baghdad-to-brooklyn/"
     target="_blank" rel="noopener noreferrer">
    <span class="ly-kirkus__stamp">Get It</span>
    <span class="ly-kirkus__who">Kirkus Reviews</span>
    <span class="ly-kirkus__what">Read the review &rarr;</span>
  </a>
</div>

---

## The Book

I left Baghdad to get away from buildings getting blown up. I moved to New York. My first job was in the World Trade Center. Then 9/11 happened.

A boy grows up in Al-Dora, in a house his father built by working for free. A young engineer leaves Iraq in 1998 with a borrowed $700 and a passport someone else is holding. A new New Yorker walks into the World Trade Center on March 26, 2001. *Baghdad to Brooklyn* is the story of what happened next, and the ten years of waiting that followed.

Above all, it is a story about what it means to rebuild a life — brick by brick, borough by borough — from Baghdad to Brooklyn.

## Three cities, one story

The book moves through three cities, and so does this site:

- **[Baghdad](/baghdad/)** · 1972–1998 — family, war, sanctions, and a childhood spent dreaming of somewhere else.
- **[Dubai](/dubai/)** · 1998–2001 — the first exit, and the slow assembly of a life from nothing.
- **[New York](/new-york/)** · 2001–present — the Twin Towers, September 11, and ten years of asylum limbo.

---

## Author's Note

> "I started writing *From Baghdad to New York* as a blog in 2002 because I wanted the world to know that Iraqis were real people — not abstractions, not statistics, not collateral damage. Years later, I realised those blog posts were the first draft of something much longer. This book is that something."
>
> — Laith Yousif

---

## Publication

| | |
|---|---|
| **Status** | Print edition available now |
| **Publisher** | Manhattan Book Group |
| **Release Date** | August 25, 2026 |
| **ISBN** | 979-8950391057 |
| **ASIN** | B0HHG9M6J1 |
| **Buy** | [Amazon]({{ amazon_url }}) |

---

## Excerpt
{: #excerpt }

*Coming soon.*

---

## Reviews

***Kirkus Reviews*** made *Baghdad to Brooklyn* a **"Get It"** pick — [read the full review](https://www.kirkusreviews.com/book-reviews/laith-yousif/baghdad-to-brooklyn/).

## For press &amp; media
{: #press }

<div class="ly-home">
  <div class="ly-press">
    <h3>Journalists, producers &amp; booking editors</h3>
    <p>
      The press kit has the bio, three story angles, book details, interview
      availability and a downloadable one-sheet. Laith is available for
      readings, panels, podcasts and interviews — especially around the 25th
      anniversary of September 11, 2026. No gatekeeper — email goes straight
      to him.
    </p>
    <dl class="ly-press__contact">
      <dt>Press contact</dt>
      <dd><a href="mailto:Laith@LaithYousif.com?subject=Press%20enquiry%20%E2%80%94%20Baghdad%20to%20Brooklyn">Laith@LaithYousif.com</a></dd>
    </dl>
    <div class="ly-press__links">
      <a class="ly-btn ly-btn--primary" href="{{ '/press/' | relative_url }}">Open the press kit &rarr;</a>
      <a class="ly-btn ly-btn--ghost" href="{{ '/press/Baghdad_to_Brooklyn_Anniversary_One_Sheet.pdf' | relative_url }}">
        <i class="fas fa-file-pdf" aria-hidden="true"></i> One-sheet (PDF)
      </a>
    </div>
  </div>
</div>

---

## Updates

Follow the writing journey through the [Baghdad To Brooklyn blog posts](/categories/baghdad-to-brooklyn/).

---

[← Back to Home](/)
