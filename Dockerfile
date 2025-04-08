# Use official Nginx image
FROM nginx:alpine

# Copy frontend files to Nginx's default HTML directory
COPY pages /usr/share/nginx/html
COPY assets /usr/share/nginx/html/assets

# Expose port 80 for frontend access
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
