# Project Overview

This repository contains coding exercises solutions implemented in Go and Python, an LLM-based question solver, and system design of past professional projects.

## Repository Structure

### LLM Solver (`llm_solver/`)

An LLM-powered solution generator that uses Claude to analyze and solve coding exercises.

#### Model used:
claude-3-5-sonnet-20240620

#### Cause of death:
Claude makes mistakes when generating test cases - a crucial step when composing a solution
I wanted it to solve excessive with minimal user friction and high reliability - Claude is not reliable enough

#### Solution Ideas:
Maintain a collection of exercises and their solutions. Use Claude to find similar exercises(few shot classification)  

#### Structure:

- **src/**
  - `anthropic_client.py` - Wrapper for Anthropic's Client
  - `solver.py` - Core solution generation logic
  - `prompts/` - Contains prompt templates for:
    - Test case generation
    - Initial problem analysis
    - System instructions

- **run/**
  - `cache/` - Caches API responses
  - `experiments/` - Experimental results and analysis
  - `input/` - Input problems for processing
  - `logs/` - Execution logs

### Go Solutions (`go_solutions/`)

coding exercises solutions implemented in Go

### Python Solutions (`py_solutions/`)

coding exercises solutions implemented in Python

### System Design Charts (`system_design_charts/`)

Collection of system design diagrams
