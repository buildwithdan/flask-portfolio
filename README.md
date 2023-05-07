# ✨Flask Portfolio website

![visitors](https://visitor-badge.laobi.icu/badge?page_id=buildwithdan.flask-portfolio)  
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/buildwithdan/flask-portfolio)  
[Docker Image](https://hub.docker.com/r/buildwithdan/flask-portfolio)

# Stack

- **Framework**: [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- **Database**: not applicable
- **Authentication**: not applicable
- **Deployment**: [Vercel](https://vercel.com)
- **Styling**: [Bootstrap](https://getbootstrap.com/)
- **Analytics**: [Vercel Analytics](https://vercel.com/analytics)

## TODO

- [x] Visitors counter badge added to main page
- [x] Fix the Vercel deploy button
- [x] updating blog and projects looping
- [x] Adding in Published Yes and No trigger, to keep certain blog posts off.
- [x] Adding view counter to blog pages
- [x] Creating a docker image for this

## Markdown files are used for blog and projects posts.

You can use https://markdownlivepreview.com/ to assist in writing markdown pages.  
Blog posts = [Where .md blog posts should be saved](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/posts)  
Projects = [Where .md projects should be saved](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/projects)

### Your Blog markdown file layout; [Example](https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/content/posts/Blog-1.md?token=GHSAT0AAAAAACAGIQ5MGJYUPQFFRHX2RDR6ZBLBG7A)

_title_: Blog1*Markdown Cheat Sheet  
\_date*: 2022-03-30

### Your Project markdown file layout; [Example](https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/content/projects/project-1.md?token=GHSAT0AAAAAACAGIQ5MPUJGDAFDBRJUIJXYZBLBGOQ)

_title_: Personal Portfolio Website  
_shortDesc_: Creating a portfolio website using Flask (micro-framework), and making it a template for others.  
_date_: 2023-03-27  
_tech_: Python, Flask, Bootstrap  
_codeLink_: https://github.com/buildwithdan/flask-portfolio/  
_webLink_: https://www.danienell.com/

## Running it Locally for development

This application requires the latest python and flask to be installed.

```bash
git clone https://github.com/buildwithdan/flask-portfolio.git
cd flask-portfolio
flask --debug --app api.index run
```

# Running it on Docker

>Read carefully!   

>This was created for educational purposes mainly, ie me getting to understand Docker and how to create images from a github project.

>If you want to change anything on the website, like name, text etc. You will need to clone OR fork this [Project on Github](https://github.com/buildwithdan/flask-portfolio), then amend the html documents in "api/templates".   

Then you can rebuild the docker image and then deploy as needed. Go into the project folder where the dockerfile is located and run this.   
```docker build -t appname .``` 

This docker image was created in such a way, to allow for adding the Markdown files for the <strong>blogs</strong> and <strong>projects</strong> locally in your docker host machine. This is achieved by created a symlink between the container folder and the host system.   

In the "docker run" command below you will see:   
Both the part in bold will need to be replaced with a location in your local machine.You can create a folder for each and then use ```pwd``` command in your terminal to find the location, after your created
 - -v <strong>/path/to/blogs</strong>:/app/api/content/posts \
 - -v <strong>/path/to/projects</strong>:/app/api/content/projects \

As example:
 - -v <strong>Users/dnell/documents/website/blog</strong>:/app/api/content/posts
 - -v <strong>Users/dnell/documents/website/projects</strong>:/app/api/content/projects

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=flask-portfolio \
  -p 5002:5000 \
  -v /path/to/blogs:/app/api/content/posts \
  -v /path/to/projects:/app/api/content/projects \
  --restart unless-stopped \
  buildwithdan/flask-portfolio

```

## Cloning / Forking

Please review the [license](https://github.com/buildwithdan/flask-portfolio/blob/simple/LICENSE.md) and remove all of my personal information (resume, blog posts, images, etc.).
