import Keycloak from "keycloak-js";

const keycloak = new Keycloak({
  url: "http://localhost:8080",
  realm: "aml-risk",
  clientId: "aml-frontend",
});

export default keycloak;
