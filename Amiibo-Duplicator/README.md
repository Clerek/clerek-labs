# Amiibo Duplication Utility

A PowerShell utility designed to automate the organization and duplication of Amiibo binary files while minimizing repetitive manual file management.

## Overview

This script recursively scans a specified directory for Amiibo `.bin` files, creates corresponding subdirectories and generates a configurable number of copies with randomized UIDs.

The script preserves original files and prevents unnecessary duplication when executed multiple times.

## Features

- Recursive directory scanning
- Automated folder creation
- Configurable duplication quantity
- Randomized Amiibo UIDs
- Original file preservation
- Existing file detection
- Duplicate processing prevention
- Automatic exclusion of non-binary files
- Execution summary and reporting

## Requirements

- Windows PowerShell or PowerShell
- Existing Amiibo binary files
- Read and write access to the target directory

## Usage

1. Download `AmiiboBulkGenerator.py`.
2. Open the script in a text editor.
3. Modify the `$root` variable to point to your Amiibo directory.
4. Modify the `$count` variable to specify the desired number of copies.
5. Save the script.
6. Open PowerShell and navigate to the script's location.
7. Execute `.\AmiiboBulkGenerator.py`.

## Repeat Execution

The script detects previously generated files and skips existing copies.

For example, if the script previously generated 13 copies and the configured quantity is increased to 50, the next execution will generate only the remaining 37 copies.

## Development Objectives

This project demonstrates practical PowerShell development through recursive file discovery, conditional logic, binary file manipulation, directory management and repeatable automation.

## Disclaimer

This utility is intended for educational purposes and personal use with legally obtained Amiibo files. No Amiibo binary files are included in this repository. This project is not affiliated with Nintendo.
