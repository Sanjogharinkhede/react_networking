# Footer Component

A responsive footer component with social media links and contact information.

## Components

### Base.jsx
The main footer component that renders the copyright text and social links.

### FootLi.jsx
A list item component that renders either a Font Awesome icon or an image with a link.

Props:
- `className`: CSS classes for styling
- `href`: URL for the link
- `icon`: Font Awesome icon object
- `src`: Image source URL (used when icon is not provided)
- `innerStyle`: Style object for the icon/image

### FootUl.jsx
A list component that renders the social media links using FootLi components.

Props:
- `className`: CSS classes for styling

## Usage

```jsx
import Footer from './components/Footer/Base';

function App() {
  return (
    <div>
      <Footer />
    </div>
  );
}
```

## Customization

To add or modify social media links, update the `CONTACT_LIST` in `src/constants/ListOfContacts.js`.

## Dependencies

- Font Awesome (configured in `src/utils/fontAwesomeConfig.js`)
- Bootstrap for styling 