// Array to store the icons
const iconImages = [
    'dumbbell.png', 'apple.png', 'yoga.png', 'water-bottle.png', 'heart.png',
    'dumbbell.png', 'apple.png', 'yoga.png', 'water-bottle.png', 'heart.png',
    'dumbbell.png', 'apple.png', 'yoga.png'
  ];
  
  // Function to generate icons dynamically and position them randomly
  function generateIcons() {
    const container = document.querySelector('.background-icons');
    
    iconImages.forEach((iconImage, index) => {
      // Create the icon div
      const icon = document.createElement('div');
      icon.classList.add('icon');
      icon.style.backgroundImage = `url(${iconImage})`;
      
      // Randomly set position on the screen
      const randomX = Math.random() * 100; // Random horizontal position (0 to 100%)
      const randomY = Math.random() * 100; // Random vertical position (0 to 100%)
      const randomDelay = Math.random() * 5; // Random animation delay for variety
  
      // Apply styles to make the icons move randomly
      icon.style.left = `${randomX}%`;
      icon.style.top = `${randomY}%`;
      icon.style.animationDelay = `${randomDelay}s`;
  
      container.appendChild(icon);
    });
  }
  
  // Call the function to generate icons when the page loads
  generateIcons();
  