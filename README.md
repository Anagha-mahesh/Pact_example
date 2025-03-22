# **Pact Testing with Consumers and Providers**

**Start Broker and Database**
- docker-compose up -d

**Publish Pacts**
- docker run --rm -v $(pwd)/pacts:/pacts pactfoundation/pact-cli \
  publish /pacts --consumer-app-version 1.0.0 --broker-base-url http://host.docker.internal:9292
  
**Verify Providers**
- docker run --rm pactfoundation/pact-cli pact-provider-verifier \
  --provider "provider name" --provider-base-url='url of provider' \
  --pact-broker-base-url=http://host.docker.internal:9292 \
  --publish-verification-results --provider-app-version=1.0.0
  
**Stop Services**
- docker-compose down

**Access Pact Broker**
- URL: http://localhost:9292
