# SOLID Design Principles

This repository coincides with the Lynda.com course Learning S.O.L.I.D. Programming Principles

## What Could Go Wrong

Software is always in a state of flux
OO Languages allow for separation of concerns
SOLID shows separation techniques and ways to avoid ripple effects

## Blackjack Sim / Intro to SOLID

The SOLID principles give programmers a common framework for addressing specific kinds of design deficiencies.

Problems with blackjack sim:
Mixed responsibilities,
Missing responsibilities,
Limited resue potential,
Not substitutable,
Poor constructor design,
Haphazard interface.

SOLID addresses software design issues

The SOLID principles give programmers a common framework for addressing specific kinds of design deficiencies.

S: Single responsibility, O: Open/closed, L: Liskov substitution, I: Interface segregation, and D: Dependency inversion.

DRY (Dont Repeat Yourself)
GRASP (General responsibility assignment software principles)
TDD (Test-driven Development)

SOLID, DRY, GRASP, and TDD overlap in principle.

The SOLID principles will help a designer articulate why some designs are superior to others. These principles will say nothing about a large number of software engineering issues.

## Interface Segregation

a client should depend on the smallest set of interface features, the fewest methods and attributes. A class needs to be designed so that collaborators have the narrowest interface.

Interface segregation tends to come down firmly on the side of wrapping any generic built-in class. This leads to classes which delegate their methods to the built-in class. The wrapping technique provides a limited interface.

Interface segregation often leads to separating a builder function or class to construct complex objects. This will segregate the interface for constructing an object from the interface for ordinary use of the object in the application.

The interface segregation principle looks at each class from the viewpoint of the collaborating classes. Taking each collaborator as a reference point, it's important to ask, "What methods and attributes does "this collaborator require?" This helps locate a cohesive, minimal interface for each collaborator.
