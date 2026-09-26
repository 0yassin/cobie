import { MeshGradient } from '@paper-design/shaders-react'
import './App.css'

function App() {
  return (
    <main className='relative min-h-screen w-screen overflow-hidden pb-36 text-white font-sans'>
      <div className='absolute inset-0 w-full h-full z-0'>
        <MeshGradient
          style={{ width: '100%', height: '100%' }}
          colors={["#121212", "#241d9a", "#121212"]}
          distortion={0.8}
          swirl={0.03}
          grainMixer={0.44}
          grainOverlay={0.11}
          speed={0.56}
        />
      </div>

      <div className='relative z-10 flex flex-col min-h-screen w-screen items-center text-center'>
        <nav className='w-full backdrop-blur-xl z-20 h-fit border-b content-center items-center border-[#F8F7F5]/40 flex justify-between pl-8 bg-[#E5E4E2]/10'>
          <span className="text-[26px] font-medium">Cobie</span>
          <div className='flex gap-0 h-full'>
            <button className='px-8 h-full hover:bg-[#F8F7F5]/20 py-4 transition-colors cursor-pointer '>
              <span className='text-[#E5E4E2]'>Download</span>
            </button>
            <button className='px-8 h-full hover:bg-[#F8F7F5]/20 py-4 transition-colors cursor-pointer '>
              <span className='text-[#E5E4E2]'>Source</span>
            </button>
          </div>
        </nav>
        <div className='w-screen h-screen -mt-20 flex justify-center items-center'>
          <h1 className='text-[64px] font-medium text-[#F8F7F5]'>
            Build with Cobie
          </h1>
        </div>
        
      <div className='w-full flex justify-center  -mt-36'>
        <div className='w-[75%] backdrop-blur-xl aspect-video bg-[#1F1F25]/40 border border-[#F8F7F5]/40 rounded-2xl '></div>
      </div>
  
      <div className='w-full mt-16 flex flex-col px-8 sm:px-16 justify-center items-center '>
        <h1 className='text-[64px] font-medium text-[#F8F7F5] mb-2'>Features</h1>
        <div className='w-full grid grid-cols-1 md:grid-cols-3 gap-x-4 gap-y-2 md:max-w-[75%]'>
            <div className='transition-all hover:-translate-y-2 bg-[#111]/75 p-6 flex flex-col rounded-xl border border-[#F8F7F5]/40'>
              <h1 className='text-[20px] text-left'>you can do a lot of stuff and a lot of things</h1>
            </div>
            <div className='transition-all hover:-translate-y-2 bg-[#111]/75 p-6 flex flex-col rounded-xl border border-[#F8F7F5]/40'>
              <h1 className='text-[20px] text-left'>It's very easy to use and setup</h1>
            </div>
            <div className='transition-all hover:-translate-y-2 bg-[#111]/75 p-6 flex flex-col rounded-xl border border-[#F8F7F5]/40'>
              <h1 className='text-[20px] text-left'>you can do a lot of stuff and a lot of things</h1>
            </div>
        </div>
      </div>
      </div>
    </main>
  )
}

export default App