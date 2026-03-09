# Commit Message Guidelines

This document outlines the criteria and best practices for writing effective commit messages in this project.

## General Principles

A good commit message should be:

- **Clear and concise**: Explain what was changed and why, without unnecessary details
- **Imperative mood**: Use commands like "Add", "Fix", "Update" rather than "Added", "Fixed", "Updated"
- **Complete**: Include enough context for reviewers to understand the change without reading the code
- **Professional**: Use proper grammar, spelling, and formatting

## Structure

### Basic Format

```
type(scope): description
```

### Detailed Format

```
type(scope): description

[optional body]

[optional footer]
```

## Types

- **feat**: New feature or functionality
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style/formatting changes (no logic changes)
- **refactor**: Code restructuring without changing functionality
- **test**: Adding or modifying tests
- **chore**: Maintenance tasks, build changes, etc.
- **perf**: Performance improvements
- **ci**: CI/CD pipeline changes
- **build**: Build system or dependency changes

## Scope (Optional)

The scope specifies the part of the codebase affected:

- `api`, `ui`, `db` for major components
- `auth`, `security` for specific features
- File names or module names

## Description

- Start with a capital letter
- Keep under 50 characters when possible
- Be specific about what changed
- Use present tense, imperative mood

## Body (Optional)

- Provide additional context when the description isn't sufficient
- Explain the motivation or reasoning
- Break down complex changes
- Keep lines under 72 characters

## Footer (Optional)

- Reference issue numbers: `Closes #123`, `Fixes #456`
- Note breaking changes: `BREAKING CHANGE: description`
- Mention co-authors: `Co-authored-by: Name <email>`

## Examples

### Good Examples

```
feat(auth): Add JWT token validation for API endpoints

- Implement token verification middleware
- Add refresh token rotation
- Update error responses for invalid tokens

Closes #123
```

```
fix(ui): Resolve dropdown menu positioning on mobile devices

The menu was overlapping content on small screens due to
incorrect z-index values. Updated CSS to use proper layering.
```

```
docs(readme): Update installation instructions for Python 3.9

- Add note about virtual environment setup
- Clarify dependency installation steps
- Update minimum Python version requirement
```

### Bad Examples

```
fixed bug
```

*Too vague, no context*

```
Added new feature for user authentication with JWT tokens and database integration plus some UI improvements
```

*Too long, mixes multiple changes*

```
feat: user login
```

*Lacks detail, doesn't explain what was implemented*

## Project-Specific Guidelines

- Always include issue references when applicable
- Use `docs:` prefix for README and documentation changes
- Group related changes in single commits when possible
- Use bullet points in body for multi-part changes
- Keep commits atomic (one logical change per commit)

## Tools and Validation

Consider using tools like:

- `commitizen` for interactive commit message creation
- `commitlint` for automated validation
- Pre-commit hooks to enforce standards

## References

- [Conventional Commits](https://conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
