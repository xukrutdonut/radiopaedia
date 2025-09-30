// Radiopaedia Viewer Application
class RadiopaediaViewer {
    constructor() {
        this.data = null;
        this.currentCase = null;
        this.currentImages = [];
        this.currentImageIndex = 0;
        this.zoom = 1;
        
        this.init();
    }

    async init() {
        // Load data
        await this.loadData();
        
        // Setup event listeners
        this.setupEventListeners();
        
        // Render case list
        this.renderCaseList();
    }

    async loadData() {
        try {
            // Try to load from scraped data
            const response = await fetch('data/playlist_data.json');
            if (response.ok) {
                this.data = await response.json();
            } else {
                // Load sample data if no scraped data exists
                this.data = this.getSampleData();
            }
        } catch (error) {
            console.error('Error loading data:', error);
            this.data = this.getSampleData();
        }
    }

    getSampleData() {
        // Sample data structure for demonstration
        return {
            id: '85715',
            title: 'Sample Medical Imaging Playlist',
            description: 'Educational cases for medical imaging',
            cases: [
                {
                    id: '1',
                    title: 'Case 1: Brain MRI',
                    presentation: 'This case demonstrates a typical brain MRI scan with various sequences.',
                    diagnosis: 'Normal brain anatomy',
                    images: [
                        {
                            url: 'https://via.placeholder.com/800x600/667eea/ffffff?text=Brain+MRI+T1',
                            alt: 'Brain MRI - T1 weighted',
                            title: 'T1 weighted sequence'
                        },
                        {
                            url: 'https://via.placeholder.com/800x600/764ba2/ffffff?text=Brain+MRI+T2',
                            alt: 'Brain MRI - T2 weighted',
                            title: 'T2 weighted sequence'
                        }
                    ]
                },
                {
                    id: '2',
                    title: 'Case 2: Chest CT',
                    presentation: 'CT scan of the chest showing normal anatomical structures.',
                    diagnosis: 'Normal chest anatomy',
                    images: [
                        {
                            url: 'https://via.placeholder.com/800x600/48bb78/ffffff?text=Chest+CT+Axial',
                            alt: 'Chest CT - Axial view',
                            title: 'Axial view'
                        },
                        {
                            url: 'https://via.placeholder.com/800x600/38ada9/ffffff?text=Chest+CT+Coronal',
                            alt: 'Chest CT - Coronal view',
                            title: 'Coronal view'
                        }
                    ]
                },
                {
                    id: '3',
                    title: 'Case 3: Abdominal MRI',
                    presentation: 'Abdominal MRI demonstrating liver and adjacent structures.',
                    diagnosis: 'Normal abdominal anatomy',
                    images: [
                        {
                            url: 'https://via.placeholder.com/800x600/f39c12/ffffff?text=Abdominal+MRI+T1',
                            alt: 'Abdominal MRI - T1',
                            title: 'T1 weighted'
                        }
                    ]
                }
            ]
        };
    }

    setupEventListeners() {
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', (e) => this.filterCases(e.target.value));

        // Modal controls
        const modal = document.getElementById('imageModal');
        const closeBtn = document.querySelector('.close');
        const prevBtn = document.getElementById('prevImage');
        const nextBtn = document.getElementById('nextImage');
        const zoomInBtn = document.getElementById('zoomIn');
        const zoomOutBtn = document.getElementById('zoomOut');
        const resetZoomBtn = document.getElementById('resetZoom');

        closeBtn.addEventListener('click', () => this.closeModal());
        prevBtn.addEventListener('click', () => this.navigateImage(-1));
        nextBtn.addEventListener('click', () => this.navigateImage(1));
        zoomInBtn.addEventListener('click', () => this.adjustZoom(0.2));
        zoomOutBtn.addEventListener('click', () => this.adjustZoom(-0.2));
        resetZoomBtn.addEventListener('click', () => this.resetZoom());

        // Close modal on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                this.closeModal();
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (modal.classList.contains('active')) {
                if (e.key === 'Escape') this.closeModal();
                if (e.key === 'ArrowLeft') this.navigateImage(-1);
                if (e.key === 'ArrowRight') this.navigateImage(1);
            }
        });
    }

    renderCaseList() {
        const caseList = document.getElementById('caseList');
        caseList.innerHTML = '';

        if (!this.data || !this.data.cases || this.data.cases.length === 0) {
            caseList.innerHTML = '<div class="loading">Loading cases</div>';
            return;
        }

        this.data.cases.forEach(caseItem => {
            const caseElement = document.createElement('div');
            caseElement.className = 'case-item';
            caseElement.dataset.caseId = caseItem.id;
            
            caseElement.innerHTML = `
                <h3>${caseItem.title || `Case ${caseItem.id}`}</h3>
                <p>${caseItem.diagnosis || caseItem.presentation?.substring(0, 60) + '...' || 'Click to view details'}</p>
            `;

            caseElement.addEventListener('click', () => this.selectCase(caseItem));
            caseList.appendChild(caseElement);
        });
    }

    filterCases(searchTerm) {
        const caseItems = document.querySelectorAll('.case-item');
        const term = searchTerm.toLowerCase();

        caseItems.forEach(item => {
            const title = item.querySelector('h3').textContent.toLowerCase();
            const description = item.querySelector('p').textContent.toLowerCase();
            
            if (title.includes(term) || description.includes(term)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    selectCase(caseData) {
        this.currentCase = caseData;
        
        // Update active state in sidebar
        document.querySelectorAll('.case-item').forEach(item => {
            item.classList.remove('active');
            if (item.dataset.caseId === caseData.id) {
                item.classList.add('active');
            }
        });

        // Render case details
        this.renderCaseDetails();
    }

    renderCaseDetails() {
        const viewer = document.getElementById('caseViewer');
        
        if (!this.currentCase) {
            viewer.innerHTML = `
                <div class="welcome-message">
                    <h2>Welcome to Radiopaedia Viewer</h2>
                    <p>Select a case from the sidebar to begin viewing</p>
                </div>
            `;
            return;
        }

        const images = this.currentCase.images || [];
        this.currentImages = images;

        viewer.innerHTML = `
            <div class="case-details">
                <h2 class="case-title">${this.currentCase.title || `Case ${this.currentCase.id}`}</h2>
                
                ${this.currentCase.presentation ? `
                    <div class="case-section">
                        <h3>Presentation</h3>
                        <p>${this.currentCase.presentation}</p>
                    </div>
                ` : ''}
                
                ${this.currentCase.diagnosis ? `
                    <div class="case-section">
                        <h3>Diagnosis</h3>
                        <p>${this.currentCase.diagnosis}</p>
                    </div>
                ` : ''}
                
                ${images.length > 0 ? `
                    <div class="case-section">
                        <h3>Medical Images (${images.length})</h3>
                        <div class="image-gallery" id="imageGallery"></div>
                    </div>
                ` : '<div class="case-section"><p>No images available for this case</p></div>'}
            </div>
        `;

        // Render image gallery
        if (images.length > 0) {
            this.renderImageGallery();
        }
    }

    renderImageGallery() {
        const gallery = document.getElementById('imageGallery');
        if (!gallery) return;

        gallery.innerHTML = '';

        this.currentImages.forEach((image, index) => {
            const galleryItem = document.createElement('div');
            galleryItem.className = 'gallery-item';
            
            galleryItem.innerHTML = `
                <img src="${image.url}" alt="${image.alt || 'Medical Image'}" loading="lazy">
                <div class="gallery-item-info">
                    <p>${image.title || image.alt || `Image ${index + 1}`}</p>
                </div>
            `;

            galleryItem.addEventListener('click', () => this.openModal(index));
            gallery.appendChild(galleryItem);
        });
    }

    openModal(imageIndex) {
        this.currentImageIndex = imageIndex;
        const modal = document.getElementById('imageModal');
        const modalImage = document.getElementById('modalImage');
        const caption = document.getElementById('imageCaption');

        const image = this.currentImages[imageIndex];
        modalImage.src = image.url;
        caption.textContent = image.title || image.alt || `Image ${imageIndex + 1}`;

        modal.classList.add('active');
        this.resetZoom();
    }

    closeModal() {
        const modal = document.getElementById('imageModal');
        modal.classList.remove('active');
        this.resetZoom();
    }

    navigateImage(direction) {
        if (this.currentImages.length === 0) return;

        this.currentImageIndex += direction;
        
        if (this.currentImageIndex < 0) {
            this.currentImageIndex = this.currentImages.length - 1;
        } else if (this.currentImageIndex >= this.currentImages.length) {
            this.currentImageIndex = 0;
        }

        const modalImage = document.getElementById('modalImage');
        const caption = document.getElementById('imageCaption');
        const image = this.currentImages[this.currentImageIndex];

        modalImage.src = image.url;
        caption.textContent = image.title || image.alt || `Image ${this.currentImageIndex + 1}`;
        this.resetZoom();
    }

    adjustZoom(delta) {
        this.zoom = Math.max(0.5, Math.min(3, this.zoom + delta));
        const modalImage = document.getElementById('modalImage');
        modalImage.style.transform = `scale(${this.zoom})`;
    }

    resetZoom() {
        this.zoom = 1;
        const modalImage = document.getElementById('modalImage');
        modalImage.style.transform = 'scale(1)';
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new RadiopaediaViewer();
});
