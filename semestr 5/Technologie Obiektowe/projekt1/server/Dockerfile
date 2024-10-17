# Use OpenJDK 17 to run the application
FROM openjdk:17-jdk-slim

# Set the working directory
WORKDIR /app

# Copy the pre-built jar file to the container
COPY target/currency-exchanger-0.0.1-SNAPSHOT.jar app.jar

# Expose the application port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
