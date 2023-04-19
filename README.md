# Flask Portfolio website

![visitors](https://visitor-badge.laobi.icu/badge?page_id=buildwithdan.flask-portfolio)  
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/buildwithdan/flask-portfolio)

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
- [ ] Creating a docker image for this

## Markdown files are used for blog and projects posts.

You can use https://stackedit.io/ to assist in writing markdown pages.  
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

## Running Locally

This application requires the latest python and flask to be installed.

```bash
git clone https://github.com/buildwithdan/flask-portfolio.git
cd flask-portfolio
flask --app api\index.py run --debug
```

## Cloning / Forking

Please review the [license](https://github.com/buildwithdan/flask-portfolio/blob/simple/LICENSE.md) and remove all of my personal information (resume, blog posts, images, etc.).
