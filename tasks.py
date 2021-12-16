
from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def robot(ctx):
    ctx.run("robot src/tests", pty=True)


@task
def tests(ctx):
    ctx.run("pytest src", pty=True)


@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
