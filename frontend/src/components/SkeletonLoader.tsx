import React from 'react';

export const SkeletonLoader: React.FC = () => {
  return (
    <div className="loading-skeleton-wrapper animate-fade-in">
      {/* Banner Skeleton */}
      <div className="skeleton-title-card">
        <div className="skeleton-pulse skeleton-h1"></div>
        <div className="skeleton-pulse skeleton-p"></div>
        <div className="skeleton-pulse skeleton-p" style={{ width: '60%' }}></div>
        <div style={{ display: 'flex', gap: '15px', marginTop: '10px' }}>
          <div className="skeleton-pulse skeleton-meta" style={{ width: '120px', height: '35px' }}></div>
          <div className="skeleton-pulse skeleton-meta" style={{ width: '120px', height: '35px' }}></div>
        </div>
      </div>

      {/* Progress Bar Skeleton */}
      <div className="skeleton-title-card" style={{ padding: '1.25rem', marginBottom: '1.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
          <div className="skeleton-pulse" style={{ height: '18px', width: '200px' }}></div>
          <div className="skeleton-pulse" style={{ height: '18px', width: '60px' }}></div>
        </div>
        <div className="skeleton-pulse" style={{ height: '10px', width: '100%', borderRadius: '999px' }}></div>
      </div>

      {/* Split Grid Skeleton */}
      <div className="skeleton-grid">
        {/* Sidebar Nav */}
        <div className="skeleton-sidebar">
          <div className="skeleton-pulse" style={{ height: '16px', width: '100px', marginBottom: '10px', marginLeft: '4px' }}></div>
          <div className="skeleton-pulse skeleton-nav-item"></div>
          <div className="skeleton-pulse skeleton-nav-item"></div>
          <div className="skeleton-pulse skeleton-nav-item"></div>
          <div className="skeleton-pulse skeleton-card" style={{ height: '120px', marginTop: '15px' }}></div>
        </div>

        {/* Content Pane */}
        <div className="skeleton-content-panel">
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
            <div className="skeleton-pulse" style={{ height: '22px', width: '80px', borderRadius: '6px' }}></div>
            <div className="skeleton-pulse skeleton-h2"></div>
          </div>
          <div className="skeleton-pulse" style={{ height: '35px', width: '100%', borderRadius: '8px' }}></div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px' }}>
            <div className="skeleton-pulse" style={{ height: '16px', width: '180px' }}></div>
            <div className="skeleton-pulse skeleton-nav-item" style={{ height: '50px' }}></div>
            <div className="skeleton-pulse skeleton-nav-item" style={{ height: '50px' }}></div>
            <div className="skeleton-pulse skeleton-nav-item" style={{ height: '50px' }}></div>
          </div>

          <div style={{ marginTop: '15px' }}>
            <div className="skeleton-pulse" style={{ height: '18px', width: '150px', marginBottom: '12px' }}></div>
            <div style={{ display: 'flex', gap: '15px' }}>
              <div className="skeleton-pulse skeleton-card" style={{ flex: 1 }}></div>
              <div className="skeleton-pulse skeleton-card" style={{ flex: 1 }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
