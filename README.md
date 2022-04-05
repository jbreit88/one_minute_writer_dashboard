<p align="center">
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
  <img src="https://user-images.githubusercontent.com/88853324/161361762-58350194-9b14-47b0-afc2-48632ef04d51.png">

</p>


# Mod4 Group Project: One Minute Writer

reference: [Project Specs and Overview](https://mod4.turing.edu/projects/capstone/expectations.html)

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#versions">Versions</a></li>
        <li><a href="#dependencies">Dependencies</a></li>
        </li>
    </li>
    </ul>
    <li>
      <a href="#project-description">About This Project</a>
      <ul>
        <li><a href="#learning-goals-for-project">Learning Goals for Project</a></li>
      </ul>
    </li>
    <li>
      <a href="#api-endpoints">One Minute Writer Dashboard Microservice</a>
      <details>
        <summary>Available Endpoints</summary>
        <ul>
          <li><a href="#dashboard-metrics">Dashboard Metrics</a></li>
          <li><a href="#update-writing-information">Update Writing Information</a></li>
        </ul>
      </details>
    </li>
    <li><a href="#collaborators">Collaborators</a></li>
  </ol>
</details>

----------

## Getting Started

### Versions

- Python 3.10.4
- Django 3.2.12

----------

### Dependencies

- [django-cors-headers](https://pypi.org/project/django-cors-headers/), [djangorestframework](https://www.django-rest-framework.org/), [psycopg2](https://pypi.org/project/psycopg2/), [gunicorn](https://docs.gunicorn.org/en/stable/run.html)

----------

### Using This Repo
This is a microservice designed to store data for and calculate user metrics for the One Minute Writer proejct app.

You can connect to this app and access the endpoints from https://enigmatic-oasis-75046.herokuapp.com/

See further documentation on accessing the [backend API](https://github.com/one-minute-writer/one_minute_writer_be) that consumes this microservice, and the user facing [frontend app](https://github.com/one-minute-writer/one_minute_writer_fe) in their respective READMEs.

----------

## Project Description

One minute writer is for creatives who are seeking inspiration and a space to document and organize their ideas and writing. They can track their progress through metrics on a user dashboard as well as revisit and edit past writings. This app was built with a cross-function team of 8 developers as the capstone proejct for graduation from the Turing School of Software and Design.

## Learning Goals for Project:

- Demonstrate knowledge gained throughout Turing
- Use an agile process to turn well defined requirements into deployed and production ready software
- Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams.
- Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing
- Practice an advanced, professional git workflow including a Pull Request Review
- Gain experience using continuous integration tools to build and automate the deployment of features
- Build applications that execute in development, test, CI, and production environments
- Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec

----------

## API Endpoints
Available endpoints (See the [Postman Collection](https://www.getpostman.com/collections/4eed83f8f6f286f882a0))

###  Dashboard Metrics

| http verb | name | description | example |
| --- | --- | --- | --- |
| GET | /dashbaord | Returns cumulative metric data for a user and their writings. Takes a comma dilineated string of id numbers as a parameter. | /dashboard?writing_ids=1,3,4,20,25 |

<details>
    <summary> JSON response example </summary>

Dashboard Metrics by User Writing IDs:
```json
  {
    "total_words_all_time": 24343,
    "total_time_all_time": 79733,
    "average_words_per_minute": 18
  }
  
```
  
</details>

### Update Writing Information

| http verb | name | description | example |
| --- | --- | --- | --- |
| POST | /dashboard| Takes updated information from writing, chunks it, and persists it to the DB. Requires writing_id, word_count, and total_time parameters | /dashboard?writing_id=25&word_count=77&total_time=190 |

<details>
  <summary> JSON response examples </summary>

Returns the object that was persisted to the databse whether newly created or updated:
```json
  {
    "writing_id": 25,
    "word_count": 27,
    "time_spent": 90,
    "created_at": "2022-03-29T14:29:42.296526-06:00"
  }

```

</details>

----------

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/JCNapier"><img src="https://avatars.githubusercontent.com/u/81737385?v=4?s=100" width="100px;" alt=""/><br /><sub><b>John Napier</b></sub></a><br /><a href="https://github.com/one-minute-writer/one_minute_writer_dashboard/commits?author=JCNapier" title="Tests">⚠️</a> <a href="https://github.com/one-minute-writer/one_minute_writer_dashboard/pulls?q=is%3Apr+reviewed-by%3AJCNapier" title="Reviewed Pull Requests">👀</a></td>

    <td align="center"><a href="https://github.com/jbreit88"><img src="https://avatars.githubusercontent.com/u/88853324?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Brad (he/him)</b></sub></a><br /><a href="https://github.com/one-minute-writer/one_minute_writer_dashboard/pulls?q=is%3Apr+reviewed-by%3Ajbreit88" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/one-minute-writer/one_minute_writer_dashboard/commits?author=jbreit88" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.
