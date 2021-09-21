
## Project Title: MovieSearch

## Description
- A search engine for movies
- Users can search for movies through the movie title, actor, director or language. The search engine will be intelligent enough to detect the type of entity is the user query and show segregated results.
- Users can also apply filters and sort by multiple attributes (year of release, review score, cast, genre etc)

## Usefulness
- The availability of multiple streaming platforms has, quite paradoxically, made the process of picking a movie to watch extremely time-consuming.
- The platforms themselves do not offer a very useful search functionality, apart from basic text search and genre-filters.
- Google search only allows you to look up a specific movie and other similar movies.
- IMDb is the closest thing to what we are trying to build. It allows user to search based on partially-matching titles and additional filters through its **Advanced Search** feature. But its filters can only be applied once and cannot be used to further refine a user query.

## Realness
- We will use IMDb's movie dataset for our search query processing.
- The dataset consists of multiple CSVs having different kinds of information on movies, all linked by a unique movie ids.
- We will use the movie ID as a foreign key to construct multiple tables and reduce data redundancy.

## Description of functionalities
### Data
We will have four tables in our database:
1. TitleTable - stores movie title, id and other attributes
2. CrewTable - stores cast and crew information for a movie
3. RatingsTable - stores ratings and review data for a movie
4. PersonTable - stores information about people and their profession
### Basic Functions
1. Search bar will support exact and partial matching of user query.
2. User query will support two types of intents - movie title and cast/crew name.
3. Results will loaded in a paginated fashion and sorted by query relevancy.
4. Supported filters - genre, language, year (slider), length (slider), rating (slider)
5. Supported sort parameters - year, length, rating
### Creative component (s)
- The IMDb dataset is refreshed daily. If time permits, we can add a background process which fetches new data daily and updates all tables in a syncronized manner.
- The search engine filters could be made dynamic according to the result set. Instead of allowing the user any possible filter, only show those filters (and their count) which are present in the result set.
### UI Mockup
