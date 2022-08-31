import { Article } from './models/article.model';

describe('Article', () => {
  it('should create an instance', () => {
    expect(new Article()).toBeTruthy();
  });
});
