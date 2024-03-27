import unittest
import subprocess
import requests, time


class TestDocker(unittest.TestCase):
    @classmethod
    def test_docker(self):
        # Launch the Docker container
        subprocess.Popen(["docker", "build", "-t", "sbose732/spam-detection", "."])
        subprocess.Popen(
            [
                "docker",
                "run",
                "-d",
                "--name",
                "spam-detection",
                "-p",
                "5000:5000",
                "sbose732/spam-detection",
            ]
        )
        # Wait for the Docker container to start
        time.sleep(40)
        # Sends a request to the Flask app running in the Docker container
        response = requests.post(
            "http://localhost:5000/score", json={"text": "Free iPhone!"}
        )
        # Check if the response is successful
        assert response.status_code == 200
        # Check if the response contains the expected keys
        assert "prediction" in response.json()
        assert "propensity" in response.json()
        # Check if the prediction is 1 (True) for an obvious spam text
        assert response.json()["prediction"] == 1
        # Close the Docker container
        subprocess.Popen(["docker", "stop", "spam-detection"])


if __name__ == "__main__":
    unittest.main()
