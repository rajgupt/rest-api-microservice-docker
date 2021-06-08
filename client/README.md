# rest-api-microservice-docker
An example of a RESTful API Deployed on a Docker Container.

This is a client API as we dont want to expose the model url and api directly to the client for different reasons.

Model API should not be concerned about xml / any other data processing as it bentoml api requests expect formatted data (dataframe / json).
