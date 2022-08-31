import { Component, OnInit } from '@angular/core';
import { Article } from 'src/app/models/article.model';
import { ArticleService } from 'src/app/services/article.service';

@Component({
  selector: 'app-add-article',
  templateUrl: './add-article.component.html',
  styleUrls: ['./add-article.component.css'],
})

export class AddArticleComponent implements OnInit {
  article: Article = { title: '', description: '', published: false };
  submitted = false;
  constructor(private articleService: ArticleService) { }
  ngOnInit(): void {
  }
  saveArticle(): void {
    const data = { title: this.article.title, description: this.article.description };
    this.articleService.create(data).subscribe({
      next: (res) => {
        console.log(res);
        this.submitted = true;
      },
      error: (err) => console.error(err)
    });
  }
  newArticle(): void {
    this.submitted = true;
    this.article = {
      title: '',
      description: '',
      published: false
    };
  }
}