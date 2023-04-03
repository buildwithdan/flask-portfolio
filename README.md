# Flask-Portfolio website

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/buildwithdan/flask-portfolio) - To still fix this..

# danienell.com

- **Framework**: [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- **Database**: not applicable
- **Authentication**: not applicable
- **Deployment**: [Vercel](https://vercel.com)
- **Styling**: [Boostrap](https://getbootstrap.com/)
- **Analytics**: [Vercel Analytics](https://vercel.com/analytics)

## TODO

- [] Fix the Vercel deploy button
- [x] updating blog and projects looping 

more to be added once its identified.

## This was setup to use Markdown files for blog and projects posts.

If you navigate to api/content you will find the folders for each;   
Blog posts = [Where .md blog posts should be saved](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/posts)   
Projects = [Where .md projects should be saved](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/projects)   

### Your Blog markdown file layout; [Example](https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/content/posts/Blog-1.md?token=GHSAT0AAAAAACAGIQ5MGJYUPQFFRHX2RDR6ZBLBG7A)
_title_: Blog1_Markdown Cheat Sheet   
_date_: 2022-03-30   
   

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
