FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1


WORKDIR /app


# System deps (build essentials for some wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
libpq-dev \
&& rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy the app code (mounted in compose too)
COPY . .


EXPOSE 8000