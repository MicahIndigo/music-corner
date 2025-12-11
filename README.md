# music-corner

## Contents

- [About](#about)
- [Rationale](#rationale)
  * [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
- [User Stories](#user-stories)
- [User Goals](#user-goals)
- [Site Structure](#site-structure)
- [Wireframes](#wireframes)
- [Design](#design)
  * [Typography](#typography)
  * [Colour Scheme](#colour-scheme)
  * [Images](#Images)
  * [Responsiveness](#responsiveness)
- [Technologies Used](#techenologies-used)
  * [Languages](#languages)
  * [Libraries and Frameworks](#libraries-and-frameworks)
  * [tools](#tools)
- [Testing](#testing)
  * [Bug Report](#bug-report)
  * [Responsiveness Test](#responsiveness-test)
  * [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
  * [User Story Testing](#user-story-testing)
  * [Features Testing](#features-testing)
  * [Accessibilty Testing](#acessibility-testing)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Browser Testing](#browser-testing)
- [Deployment](#deployment)
  * [Deploy Project](#deploy-project)
  * [Fork Project](#fork-project)
  * [Clone Project](#clone-project)
- [Credits](#credits)

## About

Music Corner is a music-focused blog and discussion platform, where users can post music-related news, write blog style updates, leave comments and interact with content.

Music corner aims to build a friendly, community-driven space where music lovers can discuss the latest releases, industry news and trending topics.

This project is built using **Django**, **PostgreSQL**, **HTML**, **CSS**, and **JavaScript** with deployment managed through **Render**.

[Back to Top](#contents)

## Rationale

The goal of this project is to create a clean, blogging platform with social interaction features, focusing specifically on music news and culture.

Django is ideal for managing user-generated content, while PostgreSQL ensures good relational data handling.

The platform is built to be expanddable, with future features such as profiles, playlists and chat/communities to be added later.

[Back to Top](#contents)

### Features

#### Existing Features
- User Authentication(Login, Register, Logout).
- Create/ Read/ Update/ Delete (CRUD) functionality for posts.
- Comment on each post.
- Upvote / Downvote system.
- Timestamp on post and comments.
- Categories for grouping content (e.g Hip-hop, R&B, Reviews, Releases).
- Responsive UI.
- Navigation bar with links to key pages.
- Clean, simple blog-style layout.

#### Future Features
- User profiles with Bios and favourite genres.
- Communities (Following/follower, Groups).
- Image Upload for posts.
- Search filters + advanced music tags (artists, albums, genres).
- API integration for Spotify/Apple Music previews.
- Dark/light theme mode.

[Back to Top](#contents)

## User Stories

- As a user, I want to create posts to share music news and updates.
- As a user, I want to read posts created by others.
- As a user, I want to comment on posts to join discussions.
- As a user, I want to upvote/downvote posts that I like or dislike.
- As a user, I want content grouped into categories so it's easier to browse.
- As a site owner, I want to build a community where users engage in discussions.

[Back to Top](#contents)

## User Goals

- Stay updated on music-related news.
- Interact with other users through comments and voting.
- Easily browse posts by category.
- Share personal insights and opinions about music.

[Back to Top](#contents)

## Site Structure

Music Corner uses a classic blog layout:

- **Homepage**: Displays a list of posts.
- **Post Page**: Full post + comments section.
- **Create Post Page**: Form for writing new posts.
- **Edit/Delete Post Pages**
- **Category Pages**: Posts filtered by genre/category.
- **User Authentication Pages**: Register, Login, Logout.

[Back to Top](#contents)