<!-- Add project logo here -->

# Mod4 Group Project: One Minute Writer

reference: [Project Specs and Overview](https://mod4.turing.edu/projects/capstone/expectations.html)

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#set-up">Set Up</a></li>
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

- [django-cors-headers](https://pypi.org/project/django-cors-headers/), [djangorestframework](https://www.django-rest-framework.org/), [psycopg2](https://pypi.org/project/psycopg2/)

----------

### Using This Repo
This is a microservice designed to store data for and calculate user metrics for the One Minute Writer proejct app.

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
    "total_words_all_time": 1142,
    "total_time_all_time": 1997
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

## Collaborators
